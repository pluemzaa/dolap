<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="lab4_3"/>
        <attribute name="authors" value="MyPC"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-22 02:42:07 AM"/>
        <attribute name="created" value="TXlQQztERVNLVE9QLTZHQkE3MEk7MjAyNS0wNy0yMjswMjozMTozMyBBTTsyNjIx"/>
        <attribute name="edited" value="TXlQQztERVNLVE9QLTZHQkE3MEk7MjAyNS0wNy0yMjswMjo0MjowNyBBTTszOzI3MzQ="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="s, e" type="Integer" array="False" size=""/>
            <output expression="&quot;Input start number: &quot;" newline="True"/>
            <input variable="s"/>
            <output expression="&quot;Input end number: &quot;" newline="True"/>
            <input variable="e"/>
            <while expression="s &lt;= e">
                <output expression="s" newline="True"/>
                <assign variable="s" expression="s+1"/>
            </while>
        </body>
    </function>
</flowgorithm>