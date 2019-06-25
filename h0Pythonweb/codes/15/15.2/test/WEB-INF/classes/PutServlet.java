package lee;

import javax.servlet.*;
import javax.servlet.http.*;
import javax.servlet.annotation.*;

import java.io.*;

@WebServlet(name="put",
    urlPatterns={"/put"})
public class PutServlet extends HttpServlet
{
	public void doPut(HttpServletRequest request ,
		HttpServletResponse response)throws IOException , ServletException
	{
		response.setContentType("text/plain");
		java.io.InputStream is = request.getInputStream();
		byte[] buff = new byte[4096];
		int len = is.read(buff);
		System.out.println(len);
		response.getOutputStream().write("Got Data:".getBytes());
		response.getOutputStream().write(buff, 0, len);
	}
}