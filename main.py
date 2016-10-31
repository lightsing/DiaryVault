from util.editor import Editor



if __name__ == '__main__':
    editor = Editor()
    editor.new_file()
    file_name = input('Load File Name:')
    editor.load_file(file_name)
