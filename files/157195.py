<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="money"/>
        <attribute name="authors" value="Admin"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-16 08:58:08 PM"/>
        <attribute name="created" value="QWRtaW47TEFQVE9QLUJLNFRIREpIOzI1NjgtMDctMTY7MDY6Mzk6MDkgUE07Mjg2Nw=="/>
        <attribute name="edited" value="QWRtaW47TEFQVE9QLUJLNFRIREpIOzI1NjgtMDctMTY7MDg6NTg6MDggUE07NDsyOTgw"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="interest, years, totalYears" type="Integer" array="False" size=""/>
            <assign variable="years" expression="1"/>
            <declare name="afterInterest, money, money1, money2, money3, amount" type="Real" array="False" size=""/>
            <output expression="&quot; Input money: &quot;" newline="True"/>
            <input variable="money"/>
            <assign variable="amount" expression="money"/>
            <output expression="&quot; Input interest (%): &quot;" newline="True"/>
            <input variable="interest"/>
            <output expression="&quot; Input years: &quot;" newline="True"/>
            <input variable="totalYears"/>
            <while expression="years &lt;= totalYears">
                <assign variable="amount" expression="amount + (amount &#215; (interest/100))"/>
                <output expression="&quot;Year &quot; &amp; years &amp; &quot;: &quot; &amp; amount" newline="True"/>
                <assign variable="years" expression="years + 1"/>
            </while>
        </body>
    </function>
</flowgorithm>