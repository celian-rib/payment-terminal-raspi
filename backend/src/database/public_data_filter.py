class PublicDataFilter():
    def to_public_dict(self, *args):
        self_dict = self.to_dict();
        tmp = {}
        for a in args:
            key = f'{a}'.split('.')[1]
            tmp[key] = self_dict[key]
        return tmp;
