class FileManager(object):
    def __init__(self, working_dir):
        self.working_dir = working_dir

    def read_file(self, path: str) -> str:
         # to read without the console
        f = open(self.working_dir + path, "r")
        redirect_text = f.read()
        f.close()
        return redirect_text
        
    def write_file(self, path, str_to_write):
        #to write without the console
        new_dir = self.working_dir + path
        f = open(new_dir, "w")
        f = open(new_dir, "a")
        f.write(str_to_write)
        f.close()
