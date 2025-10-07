<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="3281Lab4.1"/>
        <attribute name="authors" value="pppp5"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-17 01:30:06 PM"/>
        <attribute name="created" value="cHBwcDU7Q0xFTTsyMDI1LTA3LTE3OzAxOjA5OjA5IFBNOzIwNzc="/>
        <attribute name="edited" value="cHBwcDU7Q0xFTTsyMDI1LTA3LTE3OzAxOjMwOjA2IFBNOzE7MjE3Ng=="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="money, interest, years, i" type="Real" array="False" size=""/>
            <assign variable="i" expression="0"/>
            <output expression="&quot;Input money:&quot;" newline="True"/>
            <input variable="money"/>
            <output expression="&quot;Input interest (%):&quot;" newline="True"/>
            <input variable="interest"/>
            <output expression="&quot;Input years:&quot;" newline="True"/>
            <input variable="years"/>
            <while expression="i&lt;years">
                <assign variable="i" expression="i + 1"/>
                <assign variable="money" expression="money * (1 + interest / 100)"/>
                <output expression="&quot;Year &quot; &amp; i &amp; &quot;: &quot; &amp; money" newline="True"/>
            </while>
        </body>
    </function>
</flowgorithm>