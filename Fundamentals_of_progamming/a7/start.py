from src.repository.BinaryFileRepository import BinaryFileRepo
from src.repository.MemoryRepository import MemoryRepo
from src.repository.TextFileRepo import TextFileRepo
from src.services.Service import BookService
from src.ui.UI import UI


def main():

    repo = MemoryRepo()
    textRepo = TextFileRepo(file_name='file.txt')
    binaryRepo = BinaryFileRepo(file_name='file.bin')
    #repo.add()


    service = BookService(repo, textRepo,binaryRepo)
    if not textRepo.get_all():  # Check if the text file repo is empty
        service.generate_books(10, repo_type=2)

    if not binaryRepo.get_all():  # Check if the binary file repo is empty
        service.generate_books(10, repo_type=3)


    service.generate_books(10, repo_type=1)

    ui = UI(service)


    ui.start()

if __name__ == "__main__":
    main()
