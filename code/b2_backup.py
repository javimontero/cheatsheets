def b2_upload(bucket_name, filename):

    from b2sdk.v1 import InMemoryAccountInfo
    from b2sdk.v1 import B2Api

    info = InMemoryAccountInfo()
    b2 = B2Api(info)
    app_key_id = "William"
    app_key = "Gibson"
    b2.authorize_account("production", app_key_id, app_key)

    # Upload a single file
    local_file_path = filename
    b2_file_name = filename
    file_info = {"how": "good-file"}

    bucket = b2.get_bucket_by_name(bucket_name)
    bucket.upload_local_file(
        local_file=local_file_path,
        file_name=b2_file_name,
        file_infos=file_info,
    )