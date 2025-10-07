<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="myself_4"/>
        <attribute name="authors" value="ateru"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-22 06:04:08 AM"/>
        <attribute name="created" value="YXRlcnU7VEhBTlBJVENIQTsyMDI1LTA3LTIxOzEwOjI0OjI4IFBNOzI1NjU="/>
        <attribute name="edited" value="YXRlcnU7VEhBTlBJVENIQTsyMDI1LTA3LTIyOzA2OjA0OjA4IEFNOzM7MjY2Mg=="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="year, r" type="Integer" array="False" size=""/>
            <assign variable="r" expression="0"/>
            <declare name="money, ser, in, round, rate, tt, monA, interest" type="Real" array="False" size=""/>
            <assign variable="round" expression="0"/>
            <output expression="&quot;Input money: &quot;" newline="True"/>
            <input variable="money"/>
            <assign variable="monA" expression="money"/>
            <output expression="&quot;Input interest (%): &quot;" newline="True"/>
            <input variable="rate"/>
            <output expression="&quot;Input years: &quot;" newline="True"/>
            <input variable="year"/>
            <while expression="r&lt;year">
                <assign variable="interest" expression="monA*(1+(rate/100))"/>
                <assign variable="round" expression="round+interest"/>
                <output expression="&quot;Year &quot;&amp;(r+1)&amp;&quot;: &quot;&amp;interest" newline="True"/>
                <assign variable="monA" expression="interest"/>
                <assign variable="r" expression="r+1"/>
            </while>
        </body>
    </function>
</flowgorithm>