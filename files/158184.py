<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="flowtest2"/>
        <attribute name="authors" value="Acer"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-22 12:05:12 AM"/>
        <attribute name="created" value="QWNlcjtMQVBUT1AtUjUyMTQ5VlE7MjAyNS0wNy0yMTsxMTo1MDo1MSBQTTsyNjc0"/>
        <attribute name="edited" value="QWNlcjtMQVBUT1AtUjUyMTQ5VlE7MjAyNS0wNy0yMjsxMjowNToxMiBBTTs0OzI3Njk="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="money, interest, newMoney" type="Real" array="False" size=""/>
            <declare name="years, year" type="Integer" array="False" size=""/>
            <output expression="&quot;Input money:&quot;" newline="True"/>
            <input variable="money"/>
            <output expression="&quot;Input interest(%):&quot;" newline="True"/>
            <input variable="interest"/>
            <output expression="&quot;Input years:&quot;" newline="True"/>
            <input variable="years"/>
            <for variable="year" start="1" end="years" direction="inc" step="1">
                <assign variable="money" expression="money * (1+interest / 100)"/>
                <output expression="&quot;year &quot;&amp; year &amp;&quot;: &quot;&amp; money" newline="True"/>
            </for>
        </body>
    </function>
</flowgorithm>