<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="flowchart"/>
        <attribute name="authors" value="choco"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-18 01:12:17 AM"/>
        <attribute name="created" value="Y2hvY287REVTS1RPUC1QTVZSRjk5OzIwMjUtMDctMTg7MTI6NTI6MDggQU07Mjg4OA=="/>
        <attribute name="edited" value="Y2hvY287REVTS1RPUC1QTVZSRjk5OzIwMjUtMDctMTg7MDE6MTI6MTcgQU07MzsyOTky"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="i, n" type="Integer" array="False" size=""/>
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