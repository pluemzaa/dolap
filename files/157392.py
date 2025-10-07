<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="Counter_683380492-8"/>
        <attribute name="authors" value="Giyoh"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-18 02:54:42 AM"/>
        <attribute name="created" value="R2l5b2g7R0lZT0g7MjAyNS0wNy0xODswMjo0ODozMyBBTTsyMTcw"/>
        <attribute name="edited" value="R2l5b2g7R0lZT0g7MjAyNS0wNy0xODswMjo1NDo0MiBBTTsxOzIyNzU="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="n, i" type="Integer" array="False" size=""/>
            <assign variable="i" expression="0"/>
            <assign variable="n" expression="0"/>
            <output expression="&quot;Input start number: &quot;" newline="True"/>
            <input variable="i"/>
            <output expression="&quot;Input end number: &quot;" newline="True"/>
            <input variable="n"/>
            <while expression="i&lt;n">
                <output expression="i" newline="True"/>
                <assign variable="i" expression="i+1"/>
            </while>
            <output expression="i" newline="True"/>
        </body>
    </function>
</flowgorithm>