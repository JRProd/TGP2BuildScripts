import time
import threading

from P4 import P4

from . import Environment as env

# Threaded P4V Sync function
def p4_sync():
    global synced_files
    synced_files = p4.run( 'sync', '-f' )
    return synced_files

# Threaded P4v Sync callback
def p4_sync_callback( synced_files_from_p4 ):
    global files_synced
    synced_files = synced_files_from_p4
    files_synced = True

# 
threaded_callback_lock = threading.Lock()
class Threaded_Callback (threading.Thread):
    def __init__(self, thread_id, function, callback):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.function = function
        self.callback = callback
    
    def run(self):
        returnValue = self.function()

        threaded_callback_lock.acquire()
        self.callback( returnValue )
        threaded_callback_lock.release()

p4 = P4()
synced_files = {}
files_synced = False

game_name = env.get_env_variable('Game', 'game_name')

def update_from_P4( log_file ):
    log_file.write( '----------------------------------------------------------------------------------------------------\n' )
    log_file.write( '{} - Step 1: Update the local workspace for P4\n'.format( game_name ) )
    log_file.write( '----------------------------------------------------------------------------------------------------\n' )
    log_file.flush()

    # Perforce Settings
    p4.port = "129.119.63.244:1666"
    p4.user = env.get_env_variable('Perforce', 'user_name')
    p4.password = env.get_env_variable('Perforce', 'user_password')
    p4.client = env.get_env_variable('Perforce', 'client')

    # Connect to the perforce server
    success = p4.connect()
    log_file.write( str(success) )
    log_file.write('\n')
    log_file.flush()

    p4_thread = Threaded_Callback(1, p4_sync, p4_sync_callback)
    p4_thread.start()
    
    start_time = time.time()
    while( not files_synced ):
        pass

    log_file.write( 'Completed Perfoce Sync in {:.2f} seconds\n'.format( time.time() - start_time ) )
    log_file.flush()

    files_updated = 0
    files_deleted = 0
    for file in synced_files:
        if file['action'] == 'refreshed':
            continue

        if file['action'] == 'deleted':
            files_deleted += 1
            continue

        files_updated += 1
        update_message = str(files_updated) + ": "

        relative_file_name = file['clientFile']
        name_loc = relative_file_name.find( game_name )
        relative_file_name = relative_file_name[ name_loc + len(game_name):]

        update_message += relative_file_name + " ( "
        update_message += file['rev'] + " ) - "
        update_message += file['action']

        log_file.write(update_message)
        log_file.write('\n')

        if files_updated % 100 == 0:
            log_file.flush()

    if files_deleted > 0:
        log_file.write( '{} files marked for deleted in total\n'.format( files_deleted ) )
    if files_updated == 0:
        log_file.write( 'All files are current\n' )
    log_file.flush()

    return True
