<%@ page contentType="text/html" language="java" errorPage="" %>
<% 
	String name = request.getParameter("name");
	String password = request.getParameter("password");
	out.println("name参数:" + name);
	out.println("password参数:" + password);
%>