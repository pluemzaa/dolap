<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="counter"/>
        <attribute name="authors" value="prera"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-22 12:36:51 PM"/>
        <attribute name="created" value="cHJlcmE7UFJPR1JBTTsyNTY4LTA3LTIyOzEyOjMzOjE5IFBNOzIzNjk="/>
        <attribute name="edited" value="cHJlcmE7UFJPR1JBTTsyNTY4LTA3LTIyOzEyOjM2OjUxIFBNOzE7MjQ3Ng=="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="num, end" type="Integer" array="False" size=""/>
            <output expression="&quot;Input start number: &quot;" newline="True"/>
            <input variable="num"/>
            <output expression="&quot;Input end number: &quot;" newline="True"/>
            <input variable="end"/>
            <while expression="num &lt;= end">
                <output expression="num" newline="True"/>
                <assign variable="num" expression="num+1"/>
            </while>
        </body>
    </function>
</flowgorithm>