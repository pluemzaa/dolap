<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="Ex1"/>
        <attribute name="authors" value="A"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-17 09:33:51 PM"/>
        <attribute name="created" value="QTtOQVRUQVBPTkdQQzsyMDI1LTA3LTE3OzA5OjAwOjU2IFBNOzIxODQ="/>
        <attribute name="edited" value="QTtOQVRUQVBPTkdQQzsyMDI1LTA3LTE3OzA5OjMzOjUxIFBNOzE0OzIzNDU="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="year, round, much" type="Real" array="False" size=""/>
            <declare name="interest, money" type="Real" array="False" size=""/>
            <assign variable="round" expression="0"/>
            <assign variable="much" expression="0"/>
            <output expression="&quot;Input money: &quot;" newline="True"/>
            <input variable="money"/>
            <output expression="&quot;Input interest (%): &quot;" newline="True"/>
            <input variable="interest"/>
            <output expression="&quot;Input years: &quot;" newline="True"/>
            <input variable="year"/>
            <assign variable="interest" expression="interest / 100"/>
            <while expression="round &lt; year">
                <assign variable="money" expression="money*(1 + interest)"/>
                <assign variable="much" expression="much +1"/>
                <assign variable="round" expression="round + 1"/>
                <output expression="&quot;Year &quot;" newline="False"/>
                <output expression="round" newline="False"/>
                <output expression="&quot;: &quot;" newline="False"/>
                <output expression="money" newline="False"/>
                <output expression="&quot;&quot;" newline="True"/>
            </while>
        </body>
    </function>
</flowgorithm>