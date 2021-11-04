from util import readConfig

class GetUrl():
    def get_url(self):
        read=readConfig.ReadConfig()
        scheme = read.get_config('HTTP', 'scheme')
        path=read.get_config('HTTP','url')
        new_url=scheme+'://'+path
        return new_url