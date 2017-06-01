import webbrowser

x = "INDIA"

f = open('helloworld.html','w')

message = """<html>
  <head>
    <meta charset="utf-8">
    <title>My test page</title>
    <link href='http://fonts.googleapis.com/css?family=Open+Sans' rel='stylesheet' type='text/css'>
    <link href="styles/style.css" rel="stylesheet" type="text/css">
  </head>
  <body>
    <h1>Mozilla is cool</h1>
    <img src="images/firefox-icon.png" alt="The Firefox logo: a flaming fox surrounding the Earth.">

    <ul> <!-- changed to list in the tutorial -->
      <li>technologists</li>
      <li>thinkers</li>
      <li>builders</li>
    </ul>

    <table>
        <tr>
            <th>Month</th>
            <th>Savings</th>
        </tr>
        <tr>
            <td bgcolor="#FF0000">linux_distribution</td>
            <td bgcolor="#00FF00">$100</td>
        </tr>
    </table>

    <p>working together to keep the Internet alive and accessible, so people worldwide can be informed contributors and creators of the Web. We believe this act of human collaboration across an open platform is essential to individual growth and our collective future.</p>

    <p>Read the <a href="https://www.mozilla.org/en-US/about/manifesto/">Mozilla Manifesto</a> to learn even more about the values and principles that guide the pursuit of our mission.</p>
  </body>
</html>"""

f.write(message)
f.close()

#Change path to reflect file location
#filename = 'file:///C:\Users\pratik.t.patel\PycharmProjects\Databse_API' + 'helloworld.html'
#webbrowser.open_new_tab(filename)
webbrowser.open_new_tab('helloworld.html')
#webbrowser.open_new('helloworld.html')
#print "I love {}".format(x)

#C:\Users\pratik.t.patel\PycharmProjects\Databse_API