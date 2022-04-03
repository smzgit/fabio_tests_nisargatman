import psycopg2
from wiki_app import conifg_dict
from wiki_app import LOG

conn = psycopg2.connect(
    host=conifg_dict['host'],
    port=conifg_dict['port'],
    database=conifg_dict['database'],
    user=conifg_dict['user'],
    password=conifg_dict['password'])

def get_all_cities():
    try:
        cur = conn.cursor()
        cur.execute('SELECT * from cities ;')
        records = cur.fetchall()
        LOG.info("RECORDS = {}".format(records))
        return records
    except Exception as ex:
        LOG.error('Error fetching Record = {}'.format(ex))

def add_city(params):
    try:
        cur = conn.cursor()
        data=list()
        data.append(params['id'])
        data.append(params['name'])
        data.append(params['population'])
        data.append(params['area'])
        data.append(params['total_roads'])
        data.append(params['total_trees'])

        # execute a statement
        insert_query = """INSERT INTO cities (id,name,population,area,total_roads,total_trees)
                     VALUES(%s,%s,%s,%s,%s,%s) RETURNING *;"""
        cur.execute(insert_query,data)

        conn.commit()
        return True

    except Exception as ex:
        LOG.error('Error Inserting Record = {}'.format(ex))

def update_city(id,params):
    try:
        cur = conn.cursor()
        # execute a statement
        update_query = """UPDATE cities set"""
        for i,j in params.items():
            if isinstance(j,str):
                update_query+= " "+str(i)+" = '"+str(j)+"',"
            else:
                update_query += ' ' + str(i) + ' = ' + str(j) + ','
        else:
            update_query = update_query.rstrip(update_query[-1])

        update_query+= ' where id = {} ;'.format(id)

        LOG.info('Update query: {}'.format(update_query))

        cur.execute(update_query)

        conn.commit()
        return True

    except Exception as ex:
        LOG.error('Error Updating Record = {}'.format(ex))
        return False

def delete_city(id):
    try:
        cur = conn.cursor()
        # execute a statement
        del_query = """DELETE FROM cities WHERE id = {}""".format(id)

        LOG.info('DELETE query: {}'.format(del_query))

        cur.execute(del_query)

        conn.commit()
        return True

    except Exception as ex:
        LOG.error('Error Deleting Record = {}'.format(ex))
        return False

