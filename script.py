import paramiko

def connect(username, password):
    host,port = "51.255.48.54",61348
    transport = paramiko.Transport((host,port))

    transport.connect(None, username, password)
    sftp = paramiko.SFTPClient.from_transport(transport)

    return transport, sftp

def upload(localpath, serverpath, user, passwd):
    """
    Upload a file on the server
    :param localpath: Absolute path of the local file
    :param serverpath: Absolute path of the server file (extension included)
    """
    transport, sftp = connect(user, passwd)

    # Upload
    sftp.put(localpath, serverpath)

    # Close
    if sftp: sftp.close()
    if transport: transport.close()

def download(localpath, serverpath, user, passwd):
    """
    Download a file from the server
    :param localpath: Absolute path of the local file
    :param serverpath: Absolute path of the server file (extension included)
    """
    transport, sftp = connect(user, passwd)

    # Download
    sftp.get(serverpath, localpath)

    # Close
    if sftp: sftp.close()
    if transport: transport.close()

def delete(serverpath, user, passwd):
    """
    Download a file from the server
    :param serverpath: Absolute path of the server file (extension included)
    """
    transport, sftp = connect(user, passwd)

    # Download
    sftp.remove(serverpath)

    # Close
    if sftp: sftp.close()
    if transport: transport.close()

def listdir(user, passwd, serverpath="."):
    """
    Download a file from the server
    :param serverpath: Absolute path of the server folder (Current user folder by default)
    """
    transport, sftp = connect(user, passwd)

    # Download
    directory_list = [file for file in sftp.listdir(serverpath) if not file.startswith('.')]

    # Close
    if sftp: sftp.close()
    if transport: transport.close()

    return directory_list

print(listdir("ylemesle", "y\Pz=QPtg%nYZBT0keTS"))