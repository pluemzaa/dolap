<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="2"/>
        <attribute name="authors" value="tanapat"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-16 08:58:07 PM"/>
        <attribute name="created" value="dGFuYXBhdDtUQU5BUEFULVVCVU5UVTsyMDI1LTA3LTE2OzA4OjQxOjQ0IFBNOzMwODI="/>
        <attribute name="edited" value="dGFuYXBhdDtUQU5BUEFULVVCVU5UVTsyMDI1LTA3LTE2OzA4OjU4OjA3IFBNOzE7MzE5Nw=="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="money, interest, year, i" type="Real" array="False" size=""/>
            <output expression="&quot;Input money: &quot;" newline="True"/>
            <input variable="money"/>
            <output expression="&quot;Input interest (%): &quot;" newline="True"/>
            <input variable="interest"/>
            <output expression="&quot;Input years: &quot;" newline="True"/>
            <input variable="year"/>
            <assign variable="i" expression="1"/>
            <while expression="i &lt;= year">
                <assign variable="money" expression="money * (1 + (interest / 100) )"/>
                <output expression="&quot;Year &quot; &amp; i &amp; &quot;: &quot; &amp; money" newline="True"/>
                <assign variable="i" expression="i + 1"/>
            </while>
        </body>
    </function>
</flowgorithm>