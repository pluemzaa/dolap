<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="asb"/>
        <attribute name="authors" value="charp"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-16 06:12:31 PM"/>
        <attribute name="created" value="Y2hhcnA7QVNVUzsyMDI1LTA3LTE2OzA1OjU1OjIwIFBNOzIxMjY="/>
        <attribute name="edited" value="Y2hhcnA7QVNVUzsyMDI1LTA3LTE2OzA2OjEyOjMxIFBNOzE7MjIzMA=="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="a, b" type="Integer" array="False" size=""/>
            <output expression="&quot;Input start number:&quot;" newline="True"/>
            <input variable="a"/>
            <output expression="&quot;Input end number:&quot;" newline="True"/>
            <input variable="b"/>
            <while expression="a&lt;=b">
                <output expression="a" newline="True"/>
                <assign variable="a" expression="a+1"/>
            </while>
        </body>
    </function>
</flowgorithm>