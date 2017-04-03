class LRUCache(object):

    def __init__(self, size):
        self.size = size
        self.cache = {}

    def set(self, key, value):
        if len(self.cache) == self.size:
            for k, v in self.cache.items():
                v['order'] -= 1
                if v['order'] < 0:
                    self.cache.pop(k)

        self.cache[key] = {
            'value': value,
            'order': len(self.cache)
        }

    def get(self, key):
        if self.cache.get(key):
            order = self.cache.get(key)['order']
            for k, v in self.cache.items():
                if v['order'] > order:
                    v['order'] -= 1

            self.cache.get(key)['order'] = len(self.cache) - 1

            return self.cache.get(key)['value']
        else:
            return None
