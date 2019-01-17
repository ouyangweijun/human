package lee;

import javax.servlet.*;
import javax.servlet.http.*;
import javax.servlet.annotation.*;

import java.io.*;

@WebServlet(name="test",
    urlPatterns={"/test"})
public class TestServlet extends HttpServlet
{
	public void service(HttpServletRequest request ,
		HttpServletResponse response)throws IOException , ServletException
	{
		response.setContentType("text/plain");
		System.out.println("----");
		java.io.InputStream is = request.getInputStream();
		byte[] buff = new byte[4096];
		int len = is.read(buff);
		System.out.println(len);
		response.getOutputStream().write("Got Data:".getBytes());
		response.getOutputStream().write(buff, 0, len);
	}
}