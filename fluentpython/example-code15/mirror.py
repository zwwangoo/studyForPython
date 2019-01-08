class LookingGlass:
    '''
    测试LookingGlass 上下文管理器类::
        >>> from mirror import LookingGlass
        >>> with LookingGlass() as what:
        ...     print('Alice, Kitty and Showdrop')
        ...     print(what)
        ...
        pordwohS dna yttiK ,ecilA
        YKCOWREVVAJ
        >>> what
        'JAVVERWOCKY'
        >>> print('Back to normal.')
        Back to normal.
    '''
    def __enter__(self):
        import sys
        self.original_write = sys.stdout.write
        sys.stdout.write = self.reverse_write
        return 'JAVVERWOCKY'

    def reverse_write(self, text):
        self.original_write(text[::-1])

    def __exit__(self, exc_type, exc_value, traceback):
        import sys
        sys.stdout.write = self.original_write
        if exc_type is ZeroDivisionError:
            print('Please DO NOT divide by zero!')
            return True
