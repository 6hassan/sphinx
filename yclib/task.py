import luigi

def l():
    """l function"""
    return None

class A(luigi.Task):
    """
    Class A Descriptionssssss
    """
    def output(self):
        """Output of A"""
        return luigi.LocalTarget('D:\SL\sphinx\yclib\task.py')

    def run(self):
        """Run A"""
        pass