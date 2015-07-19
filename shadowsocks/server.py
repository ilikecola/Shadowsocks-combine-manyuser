import time
import sys
import thread
import server_pool
import db_transfer
import shell
import daemon
#def test():
#    thread.start_new_thread(DbTransfer.thread_db, ())
#    Api.web_server()

def main():
    shell.check_python()
    config = shell.get_config(False)
    daemon.daemon_exec(config)
    daemon.set_user(config.get('user', None))
    thread.start_new_thread(db_transfer.DbTransfer.thread_db, ())
    while True:
        time.sleep(99999)

if __name__ == '__main__':
    main()    
