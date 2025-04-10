class FileLoadError(Exception):
    """
    Исключение, возникающее при попытке загрузить несуществующий файл.

    Причина возникновения:
    - Переданный путь к файлу отсутсвует.

    Решение:
    - Убедитесь, что переданный путь введён правильно.
    """

    def __init__(self, path):
        super().__init__(f"Ошибка загрузки файла: '{path}' не найден.")
