<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="asd"/>
        <attribute name="authors" value="Anurak"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-18 10:02:05 PM"/>
        <attribute name="created" value="QW51cmFrO05BWTsyNTY4LTA3LTE3OzA4OjQ2OjI4IFBNOzIxNTA="/>
        <attribute name="edited" value="QW51cmFrO05BWTsyNTY4LTA3LTE4OzEwOjAyOjA1IFBNOzQ7MjI0Mg=="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="i, s, e" type="Integer" array="False" size=""/>
            <output expression="&quot;Input start number:&quot;" newline="True"/>
            <input variable="s"/>
            <output expression="&quot;Input end number:&quot;" newline="True"/>
            <input variable="e"/>
            <output expression="s" newline="True"/>
            <while expression="s&lt;e">
                <output expression="(s+1)" newline="True"/>
                <assign variable="s" expression="s+1"/>
            </while>
        </body>
    </function>
</flowgorithm>