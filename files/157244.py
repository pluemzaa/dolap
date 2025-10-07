<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="lab4 3333"/>
        <attribute name="authors" value="User"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-16 10:23:21 PM"/>
        <attribute name="created" value="VXNlcjtNSUROSUdIVDsyNTY4LTA3LTE2OzEwOjE4OjMxIFBNOzIzMDQ="/>
        <attribute name="edited" value="VXNlcjtNSUROSUdIVDsyNTY4LTA3LTE2OzEwOjIzOjIxIFBNOzE7MjQwNw=="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="n, i" type="Integer" array="False" size=""/>
            <output expression="&quot;Input start number: &quot;" newline="True"/>
            <input variable="i"/>
            <output expression="&quot;Input end number: &quot;" newline="True"/>
            <input variable="n"/>
            <while expression="i&lt;=n">
                <output expression="i" newline="True"/>
                <assign variable="i" expression="i+1"/>
            </while>
        </body>
    </function>
</flowgorithm>