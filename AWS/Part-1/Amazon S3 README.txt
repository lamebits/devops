
Amazon S3 is use to store and retrieve data over internet.

1. Open Amazon S3[Simple Storage Service]
2. Create Bucket [Bucket name must be unique]
3. Select Zone, enable ACL[Access Control List] for public access, off block public access from permission
4. Upload any file from computer system.
5. But still file are not public access 
	a. select file->Actions->Make public using ACL ->Make Public
6. Copy public url and check on browser.

Note : ACL should be enable and OFF Block all public access features.

##### How to host application in Amazon S3? #####

1. Download website from tooplate.
2. Create two bucket one for application hosting[barista-cafe-2137] and another for access log[barista-cafe2137-accesslog].
3. Upload all downloaded files into application hosting bucket[barista-cafe-2137].
4. Make sure ACL enable and block public access off.
5. Select all files -> Actions->Make public using ACL -> Make public.
6. Select Properties Tab of bucket:
	a. add index.html file in Static website hosting panel.
	b. Select access log bucket[barista-cafe2137-accesslog] from Server access logging.
7. Copy url from Properties -> Static website hosting panel and check in browser.

8. If you delete any files/ duplicate file uploaded from the bucket then its not permanently deleted it move to versions so enable show versions toggle and delete marker type then its automatically restored.
	
9. Life Cycle Rule:
	Go to Management of bucket and edit Life Cycle Rule where you can configure current version and noncurrent version storage management.
10. Replicate Rule: Incase if you replicate the side into another region etc. 
	Go to Management of bucket and edit it.

Note:
1. Every object nothing but files, make it public then only its accesible publically.
2. version toggle must be enable.