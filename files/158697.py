<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="3"/>
        <attribute name="authors" value="WINDOWS"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-22 07:12:41 PM"/>
        <attribute name="created" value="V0lORE9XUztMQVBUT1AtRjFJVDVWRlY7MjU2OC0wNy0yMjswNzowMToxMCBQTTsyOTIw"/>
        <attribute name="edited" value="V0lORE9XUztMQVBUT1AtRjFJVDVWRlY7MjU2OC0wNy0yMjswNzoxMjo0MSBQTTsxOzMwMzQ="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="num, end" type="Real" array="False" size=""/>
            <declare name="i, y" type="Real" array="False" size=""/>
            <output expression="&quot;Input start number:&quot;" newline="True"/>
            <input variable="num"/>
            <output expression="&quot;Input end number:&quot;" newline="True"/>
            <input variable="end"/>
            <assign variable="i" expression="num"/>
            <for variable="i" start="num" end="end" direction="inc" step="1">
                <output expression="&quot;&quot;&amp;i&amp;&quot;&quot;" newline="True"/>
            </for>
        </body>
    </function>
</flowgorithm>