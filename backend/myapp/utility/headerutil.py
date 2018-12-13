class HeaderUtil:

    @staticmethod
    def __createAlert(message, type):
        headers = {"X-Alert-Message": message, "X-Alert-Type": type}
        return headers

    @staticmethod
    def success(message):
        return HeaderUtil.__createAlert(message, "success")

    @staticmethod
    def info(message):
        return HeaderUtil.__createAlert(message, "info")

    @staticmethod
    def warning(message):
        return HeaderUtil.__createAlert(message, "warning")

    @staticmethod
    def error(message):
        return HeaderUtil.__createAlert(message, "error")