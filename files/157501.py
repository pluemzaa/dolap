<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="Lab4_4"/>
        <attribute name="authors" value="bizr"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-20 12:59:03 "/>
        <attribute name="created" value="Yml6cjtNQUNCT09LQUlSOzI1NjgtMDctMjA7IjEyOjMwOjU3ICI7MjM3MA=="/>
        <attribute name="edited" value="Yml6cjtNQUNCT09LQUlSOzI1NjgtMDctMjA7IjEyOjU5OjAzICI7MTsyNDgw"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="money, interest, newMoney" type="Real" array="False" size=""/>
            <declare name="years, year" type="Integer" array="False" size=""/>
            <output expression="&quot;Input money:&quot;" newline="True"/>
            <input variable="money"/>
            <output expression="&quot;Input interest (%):&quot;" newline="True"/>
            <input variable="interest"/>
            <output expression="&quot;Input years:&quot;" newline="True"/>
            <input variable="years"/>
            <for variable="year" start="1" end="years" direction="inc" step="1">
                <assign variable="money" expression="money * (1 + interest / 100)"/>
                <output expression="&quot;Year &quot; &amp; year &amp; &quot;: &quot; &amp; money" newline="True"/>
            </for>
        </body>
    </function>
</flowgorithm>