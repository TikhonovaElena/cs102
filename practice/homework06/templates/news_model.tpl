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
                <th>Word</th>
                %for label in labels:
                <th>{{ label }}</th>
                <th>ln(P(word|{{ label }}))</th>
                %end
            </thead>
            <tbody>
                %for word in model:
                <tr>
                    <td>{{word}}</td>
                    %for label in model[word]:
                    <td>{{model[word][label][0]}}</td>
                    <td>{{model[word][label][1]}}</td>
                    %end
                </tr>
                %end
            </tbody>
        </table>
        </div>
    </body>
</html>
