<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="ex3"/>
        <attribute name="authors" value="MY COM"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-16 11:19:27 PM"/>
        <attribute name="created" value="TVkgQ09NO0RFU0tUT1AtSEk5QUUwTTsyNTY4LTA3LTE2OzExOjA2OjUzIFBNOzI3NjA="/>
        <attribute name="edited" value="TVkgQ09NO0RFU0tUT1AtSEk5QUUwTTsyNTY4LTA3LTE2OzExOjE5OjI3IFBNOzE7Mjg3Mw=="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="n, i, end" type="Integer" array="False" size=""/>
            <output expression="&quot;Input start number:&quot;" newline="True"/>
            <input variable="i"/>
            <output expression="&quot;Input end number:&quot;" newline="True"/>
            <input variable="n"/>
            <while expression="i &lt;= n">
                <output expression="i" newline="True"/>
                <assign variable="i" expression="i+1"/>
            </while>
        </body>
    </function>
</flowgorithm>