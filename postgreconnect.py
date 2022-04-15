import psycopg2
def runquery(sql):
    try:
        connection = psycopg2.connect(user="dhaycetqhbwtxh",password="86d6d76e3c3811d2e3549cb04d56973ad55d4f35bc41ef9175c0e4d8cb9ca2c6",host="ec2-3-230-122-20.compute-1.amazonaws.com",database="d3311i8pfjjekq")
        cursor = connection.cursor()
        cursor.execute(sql)
        record = cursor.fetchall()
        return(record)
    except:
        print("Error while fetching data")
    finally:
        cursor.close()
        connection.close()
