from GUI import HomeForm
from Movies import MoviesData


def main():
    # Create First Form
    var = '''movi.nam_e'hey'''
    m = MoviesData()
    var = m.save_file_name(m, var)
    print(var)
    home_form = HomeForm()


if __name__ == '__main__':
    # Call Main Method
    main()
