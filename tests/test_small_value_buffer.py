import pytest


class SmallValueBuffer:
    def __init__(self, buffer_size=4):
        self._count = 0
        self._buffer = [0] * buffer_size
        self._wide_elements = [False] * buffer_size
        self._overflow_buffer = []
        self._overflow_wide_elements = []
        self._buffer_size = buffer_size

    def _get_wide(self, index):
        if index < self._buffer_size:
            return self._wide_elements[index]
        return self._overflow_wide_elements[index - self._buffer_size]

    def _set_wide(self, index, value):
        if index < self._buffer_size:
            self._wide_elements[index] = value
        else:
            self._overflow_wide_elements[index - self._buffer_size] = value

    def push(self, value):
        if isinstance(value, int) and value > 0xFFFFFFFF:
            return self._push_64(value)
        return self._push_32(value)

    def _push_32(self, value):
        index = self._count
        self._count += 1

        if index < self._buffer_size:
            self._buffer[index] = value
            return index

        self._overflow_buffer.append(value)
        self._overflow_wide_elements.append(False)
        return index

    def _push_64(self, value):
        # Split 64-bit value into MSB and LSB, push both to buffer
        # LSB goes at handle position, MSB implicitly at handle+1
        lsb = value & 0xFFFFFFFF
        msb = value >> 32

        lsb_index = self._push_32(lsb)
        _msb_index = self._push_32(msb)

        self._set_wide(lsb_index, True)
        return lsb_index

    def get32(self, index):
        if index < self._buffer_size:
            return self._buffer[index]
        return self._overflow_buffer[index - self._buffer_size]

    def get64(self, index):
        lsb = self.get32(index)
        msb = self.get32(index + 1)
        return (msb << 32) | lsb

    def replace(self, index, value):
        if isinstance(value, int) and value > 0xFFFFFFFF:
            return self._replace_64(index, value)
        return self._replace_32(index, value)

    def _replace_32(self, index, value):
        if index < self._buffer_size:
            self._buffer[index] = value
        else:
            self._overflow_buffer[index - self._buffer_size] = value

        # Check if we're replacing a wide (64-bit) value - need to clear MSB
        if self._get_wide(index):
            # Clear the MSB position (index + 1) and wide flag
            self._set_wide(index, False)
            msb_index = index + 1
            # Clear MSB at position + 1 (set to 0)
            if msb_index < self._buffer_size:
                self._buffer[msb_index] = 0
            elif msb_index < self._buffer_size + len(self._overflow_buffer):
                self._overflow_buffer[msb_index - self._buffer_size] = 0

        return index

    def _replace_64(self, index, value):
        lsb = value & 0xFFFFFFFF
        msb = value >> 32

        is_wide = self._get_wide(index)

        if is_wide:
            self._replace_32(index, lsb)
            # Check boundary: ensure MSB position exists
            msb_index = index + 1
            if msb_index >= self._buffer_size and msb_index >= self._buffer_size + len(
                self._overflow_buffer
            ):
                # MSB would be beyond available space - need to push instead
                return self.push(value)
            self._replace_32(index + 1, msb)
            return index
        else:
            return self.push(value)


K_BUFFER_SIZE = 4


class TestSmallValueBuffer:
    def test_copy_assignment_with_overflow(self):
        handles = [0] * (K_BUFFER_SIZE + 1)

        buffer1 = SmallValueBuffer(K_BUFFER_SIZE)
        for i in range(K_BUFFER_SIZE + 1):
            handles[i] = buffer1.push(i)

        buffer2 = SmallValueBuffer(K_BUFFER_SIZE)
        for i in range(K_BUFFER_SIZE + 1):
            buffer2._count = buffer1._count
            buffer2._buffer = buffer1._buffer.copy()
            buffer2._wide_elements = buffer1._wide_elements.copy()
            if buffer1._overflow_buffer:
                buffer2._overflow_buffer = buffer1._overflow_buffer.copy()
                buffer2._overflow_wide_elements = buffer1._overflow_wide_elements.copy()

        for i in range(K_BUFFER_SIZE + 1):
            assert buffer2.get32(handles[i]) == i

        handle = buffer1.push(42)
        assert buffer1.get32(handle) == 42

        with pytest.raises(IndexError):
            buffer2.get32(handle)

    def test_push_32(self):
        magic = 88567114

        buffer = SmallValueBuffer(K_BUFFER_SIZE)
        handle = buffer.push(magic)
        assert buffer.get32(handle) == magic

    def test_push_overflow(self):
        magic1 = 88567114
        magic2 = 351012214
        magic3 = 146122128
        magic4 = 2171092154
        magic5 = 2269016953

        buffer = SmallValueBuffer(K_BUFFER_SIZE)
        assert buffer.get32(buffer.push(magic1)) == magic1
        assert buffer.get32(buffer.push(magic2)) == magic2
        assert buffer.get32(buffer.push(magic3)) == magic3
        assert buffer.get32(buffer.push(magic4)) == magic4
        assert buffer.get32(buffer.push(magic5)) == magic5

    def test_push_64(self):
        magic = 118138934255546108

        buffer = SmallValueBuffer(K_BUFFER_SIZE)
        handle = buffer.push(magic)
        assert buffer.get64(handle) == magic

    def test_push_64_overflow(self):
        magic1 = 1401612388342512
        magic2 = 118712305386210
        magic3 = 752431801563359011
        magic4 = 118138934255546108
        magic5 = 237115443124116111

        buffer = SmallValueBuffer(K_BUFFER_SIZE)
        assert buffer.get64(buffer.push(magic1)) == magic1
        assert buffer.get64(buffer.push(magic2)) == magic2
        assert buffer.get64(buffer.push(magic3)) == magic3
        assert buffer.get64(buffer.push(magic4)) == magic4
        assert buffer.get64(buffer.push(magic5)) == magic5

    def test_push_64_after_32(self):
        magic32 = 88567114
        magic64 = 118712305386210

        buffer = SmallValueBuffer(K_BUFFER_SIZE)
        handle32 = buffer.push(magic32)
        assert buffer.get32(handle32) == magic32

        handle64 = buffer.push(magic64)
        assert buffer.get64(handle64) == magic64

    def test_push_32_after_64(self):
        magic32 = 88567114
        magic64 = 118712305386210

        buffer = SmallValueBuffer(K_BUFFER_SIZE)
        handle64 = buffer.push(magic64)
        assert buffer.get64(handle64) == magic64

        handle32 = buffer.push(magic32)
        assert buffer.get32(handle32) == magic32

    def test_replace_32_with_32(self):
        magic1 = 88567114
        magic2 = 351012214

        buffer = SmallValueBuffer(K_BUFFER_SIZE)
        handle = buffer.push(magic1)

        assert buffer.get32(buffer.replace(handle, magic2)) == magic2

    def test_replace_32_with_64(self):
        magic32 = 88567114
        magic64 = 118712305386210

        buffer = SmallValueBuffer(K_BUFFER_SIZE)
        handle = buffer.push(magic32)

        assert buffer.get64(buffer.replace(handle, magic64)) == magic64

    def test_replace_32_with_64_causes_overflow(self):
        magic1 = 88567114
        magic2 = 351012214
        magic3 = 146122128
        magic4 = 2171092154

        magic64 = 118712305386210

        buffer = SmallValueBuffer(K_BUFFER_SIZE)
        handle1 = buffer.push(magic1)
        buffer.push(magic2)
        buffer.push(magic3)
        buffer.push(magic4)

        assert buffer.get64(buffer.replace(handle1, magic64)) == magic64

    def test_replace_64_with_32(self):
        magic32 = 88567114
        magic64 = 118712305386210

        buffer = SmallValueBuffer(K_BUFFER_SIZE)
        handle = buffer.push(magic64)

        assert buffer.get32(buffer.replace(handle, magic32)) == magic32
        # Verify MSB is cleared and wide flag is reset
        assert buffer.get32(handle + 1) == 0
        assert buffer._get_wide(handle) is False

    def test_replace_64_with_64(self):
        magic1 = 1401612388342512
        magic2 = 118712305386210

        buffer = SmallValueBuffer(K_BUFFER_SIZE)
        handle = buffer.push(magic1)

        assert buffer.get64(buffer.replace(handle, magic2)) == magic2
