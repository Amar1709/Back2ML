import sys
import logging
import logger


def error_message_detail(error: str, error_detail: sys) -> str:
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = "Error occured in python script name [{0}] line number [{1}] error message = [{2}]".format(
        file_name, line_number, error
    )

    return error_message


class CustomException(Exception):
    def __init__(self, error_message: str, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(
            error_message, error_detail=error_detail
        )

    def __str__(self):
        return self.error_message
