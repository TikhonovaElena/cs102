<!DOCTYPE html>
<html>
    <head>
        <link rel="stylesheet" href="//cdnjs.cloudflare.com/ajax/libs/semantic-ui/2.2.12/semantic.min.css"></link>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/semantic-ui/2.2.12/semantic.min.js"></script>
    </head>
    <body>
        <div class="ui container" style="padding-top: 10px;">
        <table class="ui celled table">
            <thead>
                <th>Title</th>
                <th>Author</th>
                <th>#Likes</th>
                <th>#Comments</th>
            </thead>
            <tbody>
                %for g in good:
                <tr>
                    <td style="background: #dfd"><a href="{{ g.url }}">{{ g.title }}</a></td>
                    <td style="background: #dfd">{{ g.author }}</td>
                    <td style="background: #dfd">{{ g.points }}</td>
                    <td style="background: #dfd">{{ g.comments }}</td>
                </tr>
                %end
                %for m in maybe:
                <tr>
                    <td style="background: #ffc"><a href="{{ m.url }}">{{ m.title }}</a></td>
                    <td style="background: #ffc">{{ m.author }}</td>
                    <td style="background: #ffc">{{ m.points }}</td>
                    <td style="background: #ffc">{{ m.comments }}</td>
                </tr>
                %end
                %for n in never:
                <tr>
                    <td style="background: #fdd"><a href="{{ n.url }}">{{ n.title }}</a></td>
                    <td style="background: #fdd">{{ n.author }}</td>
                    <td style="background: #fdd">{{ n.points }}</td>
                    <td style="background: #fdd">{{ n.comments }}</td>
                </tr>
                %end
            </tbody>
        </table>
        </div>
    </body>
</html>
