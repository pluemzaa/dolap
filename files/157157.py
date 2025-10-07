<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="test4"/>
        <attribute name="authors" value="computer"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-16 06:22:20 PM"/>
        <attribute name="created" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDY6MTQ6NTAgUE07MjU3Nw=="/>
        <attribute name="edited" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDY6MjI6MjAgUE07MjsyNjgy"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="money" type="Real" array="False" size=""/>
            <declare name="inter, year, i" type="Integer" array="False" size=""/>
            <output expression="&quot;Input money: &quot;" newline="True"/>
            <input variable="money"/>
            <output expression="&quot;Input interest (%): &quot;" newline="True"/>
            <input variable="inter"/>
            <output expression="&quot;Input years: &quot;" newline="True"/>
            <input variable="year"/>
            <for variable="i" start="1" end="year" direction="inc" step="1">
                <assign variable="money" expression="money * (1 + inter/100)"/>
                <output expression="&quot;Year &quot; &amp;i&amp; &quot;: &quot; &amp; money" newline="True"/>
            </for>
        </body>
    </function>
</flowgorithm>