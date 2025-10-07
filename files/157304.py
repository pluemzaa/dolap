<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="002"/>
        <attribute name="authors" value="USER"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-17 03:35:15 PM"/>
        <attribute name="created" value="VVNFUjtERVNLVE9QLVBQREtFMUk7MjAyNS0wNy0xNzswMzoyOTo0NiBQTTsyNjg4"/>
        <attribute name="edited" value="VVNFUjtERVNLVE9QLVBQREtFMUk7MjAyNS0wNy0xNzswMzozNToxNSBQTTsxOzI3ODk="/>
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