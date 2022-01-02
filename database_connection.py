"""
@author: Dibyesh Mishra
@date: 30-12-2021 21:26
"""
from mysql.connector import connect, Error


class DbConnection:
    """Contains method which establishes connection with database"""

    @staticmethod
    def establish_connection():
        """
        Establish connection with database
        return: connection
        """
        mydb = connect(host="localhost", user="root", passwd="Dibyesh@3",database="student_details")
        return mydb

