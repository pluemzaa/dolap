<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="4_4"/>
        <attribute name="authors" value="MyPC"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-22 03:49:47 AM"/>
        <attribute name="created" value="TXlQQztERVNLVE9QLTZHQkE3MEk7MjAyNS0wNy0yMjswMjo0Mzo1OCBBTTsyNjMx"/>
        <attribute name="edited" value="TXlQQztERVNLVE9QLTZHQkE3MEk7MjAyNS0wNy0yMjswMjo0Njo0NyBBTTsxO015UEM7REVTS1RPUC02R0JBNzBJOzIwMjUtMDctMjI7MDI6MzE6MzMgQU07bGFiNF8zLmZwcmc7NjQ1Nw=="/>
        <attribute name="edited" value="TXlQQztERVNLVE9QLTZHQkE3MEk7MjAyNS0wNy0yMjswMzo0OTo0NyBBTTszOzI3NDY="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="m, i, y, n" type="Real" array="False" size=""/>
            <assign variable="n" expression="0"/>
            <output expression="&quot;Input money: &quot;" newline="True"/>
            <input variable="m"/>
            <output expression="&quot;Input interest (%): &quot;" newline="True"/>
            <input variable="i"/>
            <output expression="&quot;Input years: &quot;" newline="True"/>
            <input variable="y"/>
            <while expression="n&lt;y">
                <assign variable="n" expression="n+1"/>
                <assign variable="m" expression="m*(1+i/100)"/>
                <output expression="&quot;Year &quot; &amp; n &amp; &quot;: &quot; &amp; m" newline="True"/>
            </while>
        </body>
    </function>
</flowgorithm>