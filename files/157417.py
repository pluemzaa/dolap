<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="buakneung"/>
        <attribute name="authors" value="Acer"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-18 07:05:29 PM"/>
        <attribute name="created" value="QWNlcjtERVNLVE9QLTJPQkhPODg7MjU2OC0wNy0xODswNjozNzowMiBQTTsyNzE5"/>
        <attribute name="edited" value="QWNlcjtERVNLVE9QLTJPQkhPODg7MjU2OC0wNy0xODswNzowNToyOSBQTTsyOzI4MzM="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="x, snum, enum" type="Integer" array="False" size=""/>
            <output expression="&quot;Input start number:&quot;" newline="True"/>
            <input variable="snum"/>
            <output expression="&quot;Input end number:&quot;" newline="True"/>
            <input variable="enum"/>
            <output expression="snum" newline="True"/>
            <while expression="snum &lt; enum">
                <assign variable="snum" expression="snum+1"/>
                <output expression="snum" newline="True"/>
            </while>
        </body>
    </function>
</flowgorithm>