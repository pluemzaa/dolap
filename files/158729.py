<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="lab4.3"/>
        <attribute name="authors" value="Windows11"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-17 03:13:03 PM"/>
        <attribute name="created" value="V2luZG93czExO01TSTsyNTY4LTA3LTE3OzAyOjQ2OjEzIFBNOzIzNzQ="/>
        <attribute name="edited" value="V2luZG93czExO01TSTsyNTY4LTA3LTE3OzAzOjEzOjAzIFBNOzI7MjQ3Nw=="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="num1, num2, i" type="Integer" array="False" size=""/>
            <output expression="&quot;Input start number:&quot;" newline="True"/>
            <input variable="num1"/>
            <output expression="&quot;Input end number:&quot;" newline="True"/>
            <input variable="num2"/>
            <assign variable="i" expression="num1"/>
            <while expression="i&lt;=num2">
                <output expression="i" newline="True"/>
                <assign variable="i" expression="i+1"/>
            </while>
        </body>
    </function>
</flowgorithm>