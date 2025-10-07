<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="Compound Interest"/>
        <attribute name="authors" value="prabb"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-16 04:56:19 PM"/>
        <attribute name="created" value="cHJhYmI7REVTS1RPUC1WQjZCODY4OzI1NjgtMDctMTY7MDQ6NDA6NDAgUE07MjgzMQ=="/>
        <attribute name="edited" value="cHJhYmI7REVTS1RPUC1WQjZCODY4OzI1NjgtMDctMTY7MDQ6NTY6MTkgUE07MTsyOTUy"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="money, interest, years, i" type="Real" array="False" size=""/>
            <output expression="&quot;Input money: &quot;" newline="True"/>
            <input variable="money"/>
            <output expression="&quot;Input interest (%): &quot;" newline="True"/>
            <input variable="interest"/>
            <output expression="&quot;Input years: &quot;" newline="True"/>
            <input variable="years"/>
            <for variable="i" start="1" end="years" direction="inc" step="1">
                <assign variable="money" expression="money * (1 + interest/100)"/>
                <output expression="&quot;Year&quot; &amp; i &amp; &quot;: &quot;  &amp; money" newline="True"/>
            </for>
        </body>
    </function>
</flowgorithm>