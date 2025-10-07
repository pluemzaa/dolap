<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="Compound Interest_683380492-8"/>
        <attribute name="authors" value="Giyoh"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-18 03:32:15 AM"/>
        <attribute name="created" value="R2l5b2g7R0lZT0g7MjAyNS0wNy0xODswMjo1NToyMiBBTTsyMTY2"/>
        <attribute name="edited" value="R2l5b2g7R0lZT0g7MjAyNS0wNy0xODswMzozMjoxNSBBTTsyOzIyNzM="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="money, plakang, year" type="Real" array="False" size=""/>
            <declare name="i, n" type="Integer" array="False" size=""/>
            <assign variable="i" expression="0"/>
            <assign variable="n" expression="0"/>
            <assign variable="plakang" expression="0"/>
            <output expression="&quot;Input money: &quot;" newline="True"/>
            <input variable="money"/>
            <output expression="&quot;Input interest (%): &quot;" newline="True"/>
            <input variable="plakang"/>
            <assign variable="plakang" expression="plakang&#247;100"/>
            <output expression="&quot;Input years: &quot;" newline="True"/>
            <input variable="year"/>
            <while expression="i&lt;year">
                <assign variable="money" expression="money * (1 + plakang)"/>
                <assign variable="i" expression="i+1"/>
                <output expression="&quot;Year&quot;&amp;(i+0)&amp; &quot;: &quot; &amp;money" newline="True"/>
            </while>
        </body>
    </function>
</flowgorithm>