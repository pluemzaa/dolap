<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="3"/>
        <attribute name="authors" value="Windows10"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-17 10:20:28 PM"/>
        <attribute name="created" value="V2luZG93czEwO0RFU0tUT1AtSEpRNVVTQTsyNTY4LTA3LTE3OzA5OjU0OjA0IFBNOzMyNDI="/>
        <attribute name="edited" value="V2luZG93czEwO0RFU0tUT1AtSEpRNVVTQTsyNTY4LTA3LTE3OzEwOjIwOjI4IFBNOzI7MzM0Mg=="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="n, i" type="Integer" array="False" size=""/>
            <assign variable="i" expression="0"/>
            <output expression="&quot;Input start number:&quot;" newline="True"/>
            <input variable="i"/>
            <output expression="&quot;Input end number:&quot;" newline="True"/>
            <input variable="n"/>
            <while expression="i &lt;= n">
                <output expression="&quot; &quot;&amp; i &amp; &quot; &quot;" newline="True"/>
                <assign variable="i" expression="i+1"/>
            </while>
        </body>
    </function>
</flowgorithm>